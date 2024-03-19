# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for the YDF models."""

import concurrent.futures
import logging
import os
import tempfile
import textwrap
import time

from absl.testing import absltest
from absl.testing import parameterized
import numpy as np
import numpy.testing as npt
import pandas as pd

from ydf.dataset import dataset
from ydf.model import generic_model
from ydf.model import model_lib
from ydf.model import model_metadata
from ydf.model.gradient_boosted_trees_model import gradient_boosted_trees_model
from ydf.model.random_forest_model import random_forest_model
from ydf.utils import test_utils


class GenericModelTest(parameterized.TestCase):

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    # Loading models needed in many unittests.
    model_dir = os.path.join(test_utils.ydf_test_data_path(), "model")
    # This model is a Random Forest classification model without training logs.
    cls.adult_binary_class_rf = model_lib.load_model(
        os.path.join(model_dir, "adult_binary_class_rf")
    )
    # This model is a GBDT classification model without training logs.
    cls.adult_binary_class_gbdt = model_lib.load_model(
        os.path.join(model_dir, "adult_binary_class_gbdt")
    )
    # This model is a GBDT regression model without training logs.
    cls.abalone_regression_gbdt = model_lib.load_model(
        os.path.join(model_dir, "abalone_regression_gbdt")
    )

  def test_rf_instance(self):
    self.assertIsInstance(
        self.adult_binary_class_rf,
        random_forest_model.RandomForestModel,
    )
    self.assertEqual(self.adult_binary_class_rf.name(), "RANDOM_FOREST")

  def test_gbt_instance(self):
    self.assertIsInstance(
        self.adult_binary_class_gbdt,
        gradient_boosted_trees_model.GradientBoostedTreesModel,
    )
    self.assertEqual(
        self.adult_binary_class_gbdt.name(), "GRADIENT_BOOSTED_TREES"
    )

  def test_predict_adult_rf(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    predictions_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "prediction",
        "adult_test_binary_class_rf.csv",
    )

    test_df = pd.read_csv(dataset_path)
    predictions = self.adult_binary_class_rf.predict(test_df)
    predictions_df = pd.read_csv(predictions_path)

    expected_predictions = predictions_df[">50K"].to_numpy()
    npt.assert_almost_equal(predictions, expected_predictions, decimal=5)

  def test_predict_adult_gbt(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    predictions_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "prediction",
        "adult_test_binary_class_gbdt.csv",
    )

    test_df = pd.read_csv(dataset_path)
    predictions = self.adult_binary_class_gbdt.predict(test_df)
    predictions_df = pd.read_csv(predictions_path)

    expected_predictions = predictions_df[">50K"].to_numpy()
    npt.assert_almost_equal(predictions, expected_predictions, decimal=5)

  def test_predict_without_label_column(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    predictions_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "prediction",
        "adult_test_binary_class_rf.csv",
    )

    test_df = pd.read_csv(dataset_path).drop(columns=["income"])
    predictions = self.adult_binary_class_rf.predict(test_df)
    predictions_df = pd.read_csv(predictions_path)

    expected_predictions = predictions_df[">50K"].to_numpy()
    npt.assert_almost_equal(predictions, expected_predictions, decimal=5)

  def test_predict_fails_with_missing_feature_columns(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )

    test_df = pd.read_csv(dataset_path).drop(columns=["age"])
    with self.assertRaises(ValueError):
      _ = self.adult_binary_class_rf.predict(test_df)

  def test_evaluate_fails_with_missing_label_columns(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )

    test_df = pd.read_csv(dataset_path).drop(columns=["income"])
    with self.assertRaises(ValueError):
      _ = self.adult_binary_class_rf.evaluate(test_df)

  def test_evaluate_adult_gbt(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )

    test_df = pd.read_csv(dataset_path)
    evaluation = self.adult_binary_class_gbdt.evaluate(test_df)

    self.assertEqual(
        str(evaluation),
        textwrap.dedent("""\
        accuracy: 0.872351
        confusion matrix:
            label (row) \\ prediction (col)
            +-------+-------+-------+
            |       | <=50K |  >50K |
            +-------+-------+-------+
            | <=50K |  6987 |   425 |
            +-------+-------+-------+
            |  >50K |   822 |  1535 |
            +-------+-------+-------+
        characteristics:
            name: '>50K' vs others
            ROC AUC: 0.927459
            PR AUC: 0.828393
            Num thresholds: 9491
        loss: 0.279777
        num examples: 9769
        num examples (weighted): 9769
        """),
    )

  def test_analyze_adult_gbt(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )

    test_df = pd.read_csv(dataset_path)
    analysis = self.adult_binary_class_gbdt.analyze(
        test_df, permutation_variable_importance_rounds=5
    )

    self.assertEqual(
        str(analysis),
        "A model analysis. Use a notebook cell to display the analysis."
        " Alternatively, export the analysis with"
        ' `analysis.to_file("analysis.html")`.',
    )

    # Note: The analysis computation is not deterministic.
    analysis_html = analysis._repr_html_()
    self.assertIn("Partial Dependence Plot", analysis_html)
    self.assertIn("Conditional Expectation Plot", analysis_html)
    self.assertIn("Variable Importance", analysis_html)

  def test_explain_prediction_adult_gbt(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )

    test_df = pd.read_csv(dataset_path, nrows=1)
    analysis = self.adult_binary_class_gbdt.analyze_prediction(test_df)

    self.assertEqual(
        str(analysis),
        "A prediction analysis. Use a notebook cell to display the analysis."
        " Alternatively, export the analysis with"
        ' `analysis.to_file("analysis.html")`.',
    )

    analysis_html = analysis._repr_html_()
    with open("/tmp/analysis.html", "w") as f:
      f.write(analysis_html)
    self.assertIn("Feature Variation", analysis_html)

  def test_explain_prediction_adult_gbt_with_wrong_selection(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    test_df = pd.read_csv(dataset_path, nrows=3)
    with self.assertRaises(ValueError):
      _ = self.adult_binary_class_gbdt.analyze_prediction(test_df)
    with self.assertRaises(ValueError):
      _ = self.adult_binary_class_gbdt.analyze_prediction(test_df.iloc[:0])

  def test_evaluate_bootstrapping_default(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "abalone.csv"
    )
    test_df = pd.read_csv(dataset_path)
    evaluation = self.abalone_regression_gbdt.evaluate(test_df)
    self.assertIsNone(evaluation.rmse_ci95_bootstrap)

  def test_evaluate_bootstrapping_bool(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "abalone.csv"
    )
    test_df = pd.read_csv(dataset_path)
    evaluation = self.abalone_regression_gbdt.evaluate(
        test_df, bootstrapping=True
    )
    self.assertIsNotNone(evaluation.rmse_ci95_bootstrap)
    self.assertAlmostEqual(evaluation.rmse_ci95_bootstrap[0], 1.723, 2)
    self.assertAlmostEqual(evaluation.rmse_ci95_bootstrap[1], 1.866, 2)

  def test_evaluate_bootstrapping_integer(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "abalone.csv"
    )
    test_df = pd.read_csv(dataset_path)
    evaluation = self.abalone_regression_gbdt.evaluate(
        test_df, bootstrapping=599
    )
    self.assertIsNotNone(evaluation.rmse_ci95_bootstrap)
    self.assertAlmostEqual(evaluation.rmse_ci95_bootstrap[0], 1.723, 1)
    self.assertAlmostEqual(evaluation.rmse_ci95_bootstrap[1], 1.866, 1)

  def test_evaluate_bootstrapping_error(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "abalone.csv"
    )
    test_df = pd.read_csv(dataset_path)
    with self.assertRaisesRegex(ValueError, "an integer greater than 100"):
      self.abalone_regression_gbdt.evaluate(test_df, bootstrapping=1)

  def test_prefixed_model_loading_autodetection(self):
    model_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "model",
        "prefixed_adult_binary_class_gbdt",
    )
    model = model_lib.load_model(model_path)
    self.assertEqual(model.name(), "GRADIENT_BOOSTED_TREES")

  def test_prefixed_model_loading_explicit(self):
    model_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "model",
        "prefixed_adult_binary_class_gbdt",
    )
    model = model_lib.load_model(
        model_path, generic_model.ModelIOOptions(file_prefix="prefixed_")
    )
    self.assertEqual(model.name(), "GRADIENT_BOOSTED_TREES")

  def test_prefixed_model_loading_fails_when_incorrect(self):
    model_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "model",
        "prefixed_adult_binary_class_gbdt",
    )
    with self.assertRaises(test_utils.AbslInvalidArgumentError):
      model_lib.load_model(
          model_path, generic_model.ModelIOOptions(file_prefix="wrong_prefix_")
      )

  def test_model_load_and_save(self):
    model_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "model",
        "prefixed_adult_binary_class_gbdt",
    )
    model = model_lib.load_model(
        model_path, generic_model.ModelIOOptions(file_prefix="prefixed_")
    )
    with tempfile.TemporaryDirectory() as tempdir:
      model.save(tempdir, generic_model.ModelIOOptions(file_prefix="my_prefix"))
      self.assertTrue(os.path.exists(os.path.join(tempdir, "my_prefixdone")))

  def test_model_str(self):
    self.assertEqual(
        str(self.adult_binary_class_gbdt),
        """\
Model: GRADIENT_BOOSTED_TREES
Task: CLASSIFICATION
Class: ydf.GradientBoostedTreesModel
Use `model.describe()` for more details
""",
    )

  def test_model_describe_text(self):
    self.assertIn(
        'Type: "GRADIENT_BOOSTED_TREES"',
        self.adult_binary_class_gbdt.describe("text"),
    )

  def test_model_describe_html(self):
    html_description = self.adult_binary_class_gbdt.describe("html")
    self.assertIn("GRADIENT_BOOSTED_TREES", html_description)

  def test_model_to_cpp(self):
    cc = self.adult_binary_class_gbdt.to_cpp()
    logging.info("cc:\n%s", cc)

  def test_benchmark(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    test_df = pd.read_csv(dataset_path)
    benchmark_result = self.adult_binary_class_gbdt.benchmark(test_df)
    print(benchmark_result)

  def test_model_metadata(self):
    metadata = model_metadata.ModelMetadata(
        owner="TestOwner",
        created_date=31415,
        uid=271828,
        framework="TestFramework",
    )
    self.adult_binary_class_gbdt.set_metadata(metadata)
    self.assertEqual(metadata, self.adult_binary_class_gbdt.metadata())

  def test_label_col_idx(self):
    self.assertEqual(self.adult_binary_class_gbdt.label_col_idx(), 14)

  def test_label_classes(self):
    label_classes = self.adult_binary_class_gbdt.label_classes()
    self.assertEqual(label_classes, ["<=50K", ">50K"])

  def test_model_with_catset(self):
    model_path = os.path.join(
        test_utils.ydf_test_data_path(), "model", "sst_binary_class_gbdt"
    )
    model = model_lib.load_model(model_path)
    test_ds_path = "csv:" + os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "sst_binary_test.csv"
    )
    evaluation = model.evaluate(test_ds_path)
    self.assertAlmostEqual(evaluation.accuracy, 0.80011, places=5)

  def test_multi_thread_predict(self):
    dataset_path = os.path.join(
        test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
    )
    test_df = pd.read_csv(dataset_path)
    test_ds = dataset.create_vertical_dataset(
        test_df, data_spec=self.adult_binary_class_gbdt.data_spec()
    )
    for num_workers in range(1, 10 + 1):
      with concurrent.futures.ThreadPoolExecutor(num_workers) as executor:
        begin = time.time()
        _ = list(
            executor.map(self.adult_binary_class_gbdt.predict, [test_ds] * 10)
        )
        end = time.time()
        logging.info("Runtime for %s workers: %s", num_workers, end - begin)

  def test_self_evaluation_gbt(self):
    # This model is a classification model with full training logs.
    gbt_adult_base_with_na_path = os.path.join(
        test_utils.ydf_test_data_path(), "golden", "gbt_adult_base_with_na"
    )
    gbt_adult_base_with_na = model_lib.load_model(gbt_adult_base_with_na_path)
    self_evaluation = gbt_adult_base_with_na.self_evaluation()
    self.assertAlmostEqual(self_evaluation.accuracy, 0.8498403)

  def test_self_evaluation_rf(self):
    self_evaluation = self.adult_binary_class_rf.self_evaluation()
    self.assertAlmostEqual(self_evaluation.loss, 0.31474323732)

  def test_empty_self_evaluation_rf(self):
    # Uplift models do not have OOB evaluations.
    model_path = os.path.join(
        test_utils.ydf_test_data_path(),
        "model",
        "sim_pte_categorical_uplift_rf",
    )
    model = model_lib.load_model(model_path)
    self.assertIsNone(model.self_evaluation())

  def test_gbt_list_compatible_engines(self):
    self.assertContainsSubsequence(
        self.adult_binary_class_gbdt.list_compatible_engines(),
        ["GradientBoostedTreesGeneric"],
    )

  def test_rf_list_compatible_engines(self):
    self.assertContainsSubsequence(
        self.adult_binary_class_rf.list_compatible_engines(),
        ["RandomForestGeneric"],
    )

  def test_gbt_force_compatible_engines(self):
    test_df = pd.read_csv(
        os.path.join(
            test_utils.ydf_test_data_path(), "dataset", "adult_test.csv"
        )
    )
    p1 = self.adult_binary_class_gbdt.predict(test_df)
    self.adult_binary_class_gbdt.force_engine("GradientBoostedTreesGeneric")
    p2 = self.adult_binary_class_gbdt.predict(test_df)
    self.adult_binary_class_gbdt.force_engine(None)
    p3 = self.adult_binary_class_gbdt.predict(test_df)

    np.testing.assert_allclose(
        p1,
        p2,
        rtol=1e-5,
        atol=1e-5,
    )
    np.testing.assert_allclose(
        p1,
        p3,
        rtol=1e-5,
        atol=1e-5,
    )


if __name__ == "__main__":
  absltest.main()

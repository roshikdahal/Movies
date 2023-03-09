from Movies.config.configurations import DataTransformationConfig
from Movies.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from Movies.logger import logging
from sklearn.compose import ColumnTransformer
from Movies.utils import read_yaml_file
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact):
        try:
            logging.info("Data Transformation log started. ")
            self.data_transformation_config= data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact

        except Exception as e:
            return e
        

    def replace_currency(col, symbol):
        return col.str.replace(symbol, '')

    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path

            dataset_schema = read_yaml_file(file_path=schema_file_path)

            pipeline = Pipeline([
                ('currency_replacement', ColumnTransformer(
                    transformers=[
                        ('replace_dollar', FunctionTransformer(self.replace_currency, kw_args={'symbol': '$'}), dataset_schema),
                        ('replace_comma', FunctionTransformer(self.replace_currency, kw_args={'symbol': ','}), ['column_3', 'column_4'])
                    ],
                    remainder='passthrough'
                ))
            ])
            
            replaceNAN_pipeline = Pipeline(steps=[
                ('replaceNaN',dataset_schema.replace('\\N', np.nan, inplace=True))
            ])

            
            

            
            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN_KEY]


            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('feature_generator', FeatureGenerator(
                    add_bedrooms_per_room=self.data_transformation_config.add_bedroom_per_room,
                    columns=numerical_columns
                )),
                ('scaler', StandardScaler())
            ]
            )

            cat_pipeline = Pipeline(steps=[
                 ('impute', SimpleImputer(strategy="most_frequent")),
                 ('one_hot_encoder', OneHotEncoder()),
                 ('scaler', StandardScaler(with_mean=False))
            ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")


            preprocessing = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns),
            ])
            return preprocessing

        except Exception as e:
            raise HousingException(e,sys) from e       
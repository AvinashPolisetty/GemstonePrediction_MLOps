import os
import sys
from logger.logging import logging
from exception.exception import customexception
import pandas as pd

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
from components.model_evaluation import ModelEvaluation



obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

datatransformation=DataTransformation()
train_arr,test_arr=datatransformation.initialize_data_transformation(train_data_path,test_data_path)

model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

model_evaluation_obj=ModelEvaluation()
model_evaluation_obj.initiate_model_evaluation(train_arr,test_arr)


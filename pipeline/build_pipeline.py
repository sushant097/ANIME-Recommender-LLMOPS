from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()

logger = get_logger(__name__)


def main():
    try:
        logger.info("Starting the pipeline to build vector store from CSV data.")
        data_loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv", processed_csv="data/processed_anime.csv")
        processed_csv = data_loader.load_and_process() # str output path to processed CSV
        logger.info("Data loaded and processed successfully.")
        vector_store_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_store_builder.build_and_save_vectorstore()
        logger.info("Vector store built and persisted successfully.")
        logger.info("Pipeline build successfully.")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise CustomException("Pipeline failed", e)
    

if __name__ == "__main__":
    main()
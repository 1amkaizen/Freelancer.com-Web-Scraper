import argparse
import time
from scraper import scrape_freelancer_jobs


def parse_arguments():
    parser = argparse.ArgumentParser(description='Scrape Freelancer job listings')
    parser.add_argument('-p', '--pages', type=int, default=0, help='Number of pages to scrape (0 for all pages)')
    return parser.parse_args()





if __name__ == "__main__":
    args = parse_arguments()
    scrape_freelancer_jobs(args.pages)


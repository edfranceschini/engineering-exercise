import json
from datetime import datetime

from app import db, create_app
from app.models.items import Item
from app.utils.date_parser import parse_date


def load_initial_data(json_file_path):
    app = create_app()
    with app.app_context():
        with open(json_file_path, "r") as f:
            data_json = json.load(f)
            for item in data_json["items"]:
                if Item.query.filter_by(url=item["uri"]).first():
                    continue  # Skip items already in the database

                title = item.get("title")
                url = item.get("uri")  # Note the JSON field is 'uri', not 'url'
                date_str = item.get("date")

                if not all([title, url, date_str]):
                    continue  # Skip items missing any of the required fields

                date_added = parse_date(date_str)

                if not date_added:
                    print(f"Skipping due to date parsing error: {item}")
                    continue  # Skip items with unparsable dates

                new_data = Item(title=title, url=url, date_added=date_added)
                db.session.add(new_data)

                continue  # Skip items with unrecognized date formats
            db.session.commit()


if __name__ == "__main__":
    load_initial_data("input/data.json")

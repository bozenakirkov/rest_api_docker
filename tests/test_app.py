from flask import url_for

from app import app


def test_app():

    with app.test_request_context():
        assert url_for('get_stores') == "/store"
        assert url_for('delete_store', store_id="abcde") == "/store/abcde"
        assert url_for('get_store', store_id="abcde") == "/store/abcde"
        assert url_for('get_item', item_id="abcde") == "/item/abcde"



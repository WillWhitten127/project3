import pytest
from your_project import db, create_app
from your_project.models.auth_log import AuthLog

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_new_auth_log(app):
    """
    GIVEN an AuthLog model
    WHEN a new AuthLog is created
    THEN check the request_ip and user_id fields are defined correctly
    """
    log = AuthLog(request_ip='127.0.0.1', user_id=1)
    db.session.add(log)
    db.session.commit()
    assert log.request_ip == '127.0.0.1'
    assert log.user_id == 1

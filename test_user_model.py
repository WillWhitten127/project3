import pytest
from your_project import db, create_app
from your_project.models.user import User

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_new_user(app):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed password, and username fields are defined correctly
    """
    user = User(username='testuser', email='test@test.com', password_hash='hashedpassword')
    db.session.add(user)
    db.session.commit()
    assert user.username == 'testuser'
    assert user.email == 'test@test.com'
    assert user.password_hash == 'hashedpassword'

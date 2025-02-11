from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='djalmajunior',
            email='junior.silva@alu.ufc.br',
            password='12345678',
        )

        session.add(new_user)
        session.commit()

    result = session.scalar(
        select(User).where(User.email == 'junior.silva@alu.ufc.br')
    )

    assert asdict(result) == {
        'id': 1,
        'username': 'djalmajunior',
        'email': 'junior.silva@alu.ufc.br',
        'password': '12345678',
        'created_at': time,
        'updated_at': time,
    }

from flask_login import UserMixin
from sqlalchemy import create_engine, String, Integer, Float, func, Column, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

#base de dados
engine = create_engine('mysql+pymysql://root:Senaisp@localhost:3306/empresa_db')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Funcionario(Base, UserMixin):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    data_nascimento = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    cargo = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    criado_em = Column(DateTime, server_default=func.now())
# serve pra printar a classe o repr
    def __repr__(self):
        return f'<Funcionario: {self.nome}>'

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)


    def save(self, db_session):
        try:
            db_session.add(self)
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            raise
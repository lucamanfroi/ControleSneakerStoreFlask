from ..extensions import db

class Estoque(db.Model):
    __tablename__ = "estoque"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(20))
    modelo = db.Column(db.String(100))
    cor = db.Column(db.String(20))
    tamanho = db.Column(db.Integer)
    data = db.Column(db.Date)
    img_link = db.Column(db.String(300))

    def __repr__(self):
        return f"<Estoque(marca={self.marca}, modelo={self.modelo}, cor={self.cor}, tamanho={self.tamanho}, tamanho={self.tamanho}, data={self.data})>"
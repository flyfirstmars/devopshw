from app import db


class Assignment(db.Model):
    __tablename__ = "assignments"
    id = db.Column(db.Integer, primary_key=True)
    assignment_name = db.Column(db.String(), nullable=False)
    assignment_issued_date = db.Column(db.DateTime(), nullable=False)
    assignment_turnIn_date = db.Column(db.DateTime(), nullable=True)
    assignment_description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<Assignment %r>" % self.assignment_name

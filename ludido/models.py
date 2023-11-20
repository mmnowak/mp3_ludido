from ludido import db

class Users(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Occasion(db.Model):
    # schema for the Occasion model
    id = db.Column(db.Integer, primary_key=True)
    occasion_name = db.Column(db.String(50), unique=True, nullable=False)
    activities = db.relationship("Activity", backref="occasion",
                                 cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.occasion_name


class Activity(db.Model):
    # schema for the Activity model
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(50), unique=True, nullable=False)
    activity_description = db.Column(db.Text, nullable=False)
    activity_age = db.Column(db.Text, nullable=False)
    activity_type = db.Column(db.Text, nullable=False)
    activity_developmental = db.Column(db.Text, nullable=False)
    occasion_id = db.Column(db.Integer, db.ForeignKey("occasion.id",
                                                      ondelete="CASCADE"),
                            nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Activity: {1} | Age Group(s): {2} | Type: {3} | \
                 Developmental Area: {4}".format(
            self.id, self.activity_name, self.activity_age, self.activity_type,
            self.activity_developmental
        )
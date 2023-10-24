from ludido import db


class Ages(db.Model):
    # schema for the Age Groups model
    id = db.Column(db.Integer, primary_key=True)
    activities = db.relationship("Activity", backref="ages",
                                 cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Type(db.Model):
    # schema for the Activity Typr model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Development(db.Model):
    # schema for the Developmental Area model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Occasion(db.Model):
    # schema for the Occasion model
    id = db.Column(db.Integer, primary_key=True)
    activities = db.relationship("Activity", backref="occasion", cascade="all, \
                                 delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Activity(db.Model):
    # schema for the Activity model
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(50), unique=True, nullable=False)
    activity_description = db.Column(db.Text, nullable=False)
    activity_age = db.Column(db.Text, nullable=False)
    activity_type = db.Column(db.Text, nullable=False)
    activity_developmental = db.Column(db.Text, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id",
                                                      ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Activity: {1} | Age Group(s): {2} | Type: {3} | \
                 Developmental Area: {4}".format(
            self.id, self.activity_name, self.activity_age, self.activity_type,
            self.activity_developmental
        )
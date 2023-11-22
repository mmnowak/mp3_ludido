from ludido import db

class Users(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    activities = db.relationship("Activity", backref="user_activity", cascade="all, delete", lazy=True)
    occasions = db.relationship("Occasion", backref="user_occasion", cascade="all, delete", lazy=True)
    favourites = db.relationship("Favourite", backref="user_favs", cascade="all, delete", lazy=True)

    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Occasion(db.Model):
    # schema for the Occasion model
    id = db.Column(db.Integer, primary_key=True)
    occasion_name = db.Column(db.String(50), unique=True, nullable=False)
    occasion_createdby = db.Column(db.Text, db.ForeignKey("users.username",
                                                         ondelete="CASCADE"), nullable=False)
    activities = db.relationship("Activity", backref="occasion",
                                 cascade="all, delete", lazy=True)
    user = db.relationship("Users", backref="user_occasion", lazy=True)

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
    activity_createdby = db.Column(db.Text, db.ForeignKey("users.username",
                                                         ondelete="CASCADE"), nullable=False)
    occasion_id = db.Column(db.Integer, db.ForeignKey("occasion.id",
                                                      ondelete="CASCADE"),
                            nullable=False)
    user = db.relationship("Users", backref="user_activity", lazy=True)
    favourites = db.relationship("Favourite", backref="fav_activity", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Activity: {1} | Age Group(s): {2} | Type: {3} | \
                 Developmental Area: {4} | Occasion: {5} | \
                 Author: {6}".format(
            self.id, self.activity_name, self.activity_age, self.activity_type,
            self.activity_developmental, self.occasion_id, self.activity_createdby
        )


class Favourite(db.Model):
    # schema for the Favourite model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, db.ForeignKey("users.username"), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey("activity.id"), nullable=False)
    users = db.relationship("Users", backref="user_favs", lazy=True)
    activities = db.relationship("Activity", backref="fav_activity", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Username: {1} | Activity ID: {2}".format(
            self.id, self.username, self.activity_id
        )
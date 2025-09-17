// app/models/UserTable.scala
package models

import slick.jdbc.SQLiteProfile.api._
import slick.lifted.ProvenShape

// The class that defines the "users" table structure.
class UserTable(tag: Tag) extends Table[User](tag, "users") {

    // Defines a column "id" of type Long, it's the Primary Key, and it Auto Increments.
    def id: Rep[Long] = column[Long]("id", O.PrimaryKey, O.AutoInc)

    // Defines a column "name" of type String.
    def name: Rep[String] = column[String]("name")

    // Defines a column "email" of type String.
    def email: Rep[String] = column[String]("email")

    // The * projection is the mapping between the columns and the User case class.
    // It tells Slick how to convert a row from the database into a User object and back.
    def * : ProvenShape[User] = (id, name, email) <> ((User.apply _).tupled, User.unapply)
}
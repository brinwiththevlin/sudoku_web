// app/models/UserRepository.scala
package models

import play.api.db.slick.{DatabaseConfigProvider, HasDatabaseConfigProvider}
import slick.jdbc.JdbcProfile

import javax.inject.{Inject, Singleton}
import scala.concurrent.{ExecutionContext, Future}

// @Singleton ensures that only one instance of this class is created.
// @Inject tells Play's dependency injection to provide the necessary objects.
@Singleton
class UserRepository @Inject()(protected val dbConfigProvider: DatabaseConfigProvider)(implicit ec: ExecutionContext) extends HasDatabaseConfigProvider[JdbcProfile] {

    // This line brings all the Slick query operators into scope.

    import profile.api._

    // A query object for the UserTable. This is the starting point for all queries.
    private val users = TableQuery[UserTable]

    /**
     * Adds a new user to the "users" table.
     * Slick's `returning` feature is used to get back the user object with the
     * auto-generated ID from the database.
     */
    def add(user: User): Future[User] = {
        val insertQuery = (users returning users.map(_.id) into ((user, id) => user.copy(id = id))) += user
        db.run(insertQuery)
    }

    /**
     * Lists all the users from the database.
     * `users.result` is a DBIOAction that describes reading all rows.
     * `db.run` executes the action and returns a Future.
     */
    def list(): Future[Seq[User]] = {
        db.run(users.result)
    }
}
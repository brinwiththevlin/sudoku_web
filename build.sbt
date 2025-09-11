name := """sudoku"""
organization := "org.brinhasavlin"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "2.13.16"

libraryDependencies += guice
libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "7.0.2" % Test

val slickVersion = "5.1.0" // Check for the latest version

libraryDependencies ++= Seq(
    // This is the main library for Play-Slick integration
    "com.typesafe.play" %% "play-slick" % slickVersion,

    // This is the JDBC driver that allows Java/Scala to talk to SQLite
    "org.xerial" % "sqlite-jdbc" % "3.45.1.0", // Check for the latest version

    // This is for Play's dependency injection system
    guice
)
// Adds additional packages into Twirl
//TwirlKeys.templateImports += "org.brinhasavlin.controllers._"

// Adds additional packages into conf/routes
// play.sbt.routes.RoutesKeys.routesImport += "org.brinhasavlin.binders._"

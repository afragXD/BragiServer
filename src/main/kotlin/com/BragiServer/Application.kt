package com.BragiServer

import com.BragiServer.features.books.configureBooksRouting
import com.BragiServer.features.login.configureLoginRouting
import com.BragiServer.features.profile.configureProfileRouting
import com.BragiServer.features.register.configureRegisterRouting
import com.BragiServer.features.update.configureUpdate
import com.BragiServer.plugins.*
import io.ktor.server.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import org.jetbrains.exposed.sql.Database

fun main() {
    Database.connect("jdbc:postgresql://localhost:5432/bragi", driver = "org.postgresql.Driver",
        user = "postgres", password = "742617"
    )

    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module)
        .start(wait = true)
}

fun Application.module() {
    configureSerialization()
    configureRouting()
    configureHTTP()
    configureStaticRouting()

    configureRegisterRouting()
    configureLoginRouting()

    configureProfileRouting()
    configureUpdate()

    configureBooksRouting()


    configureTest()
}

package com.BragiServer.plugins

import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.http.content.*
import io.ktor.server.routing.*

fun Application.configureStaticRouting() {
    routing {
        staticResources("/static/avatars", "static/avatars"){
            default("default_avatar.png")
        }
        staticResources("/static/books", "static/books/res/novel"){
            //default("mergen.txt")
        }
    }
}

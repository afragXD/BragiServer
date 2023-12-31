package com.BragiServer.features.profile

import com.BragiServer.features.profile.ProfileController
import io.ktor.server.application.*
import io.ktor.server.routing.*

fun Application.configureProfileRouting() {
    routing {
        get("/profile") {
            val profileController = ProfileController(call)
            profileController.profileSearch()
        }
    }
}
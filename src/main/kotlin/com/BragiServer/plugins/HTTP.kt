package com.BragiServer.plugins

import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.plugins.cors.routing.*
import io.ktor.server.routing.*

fun Application.configureHTTP() {
    install(CORS){
        anyHost()
        allowHeader(HttpHeaders.ContentType)
        allowMethod(HttpMethod.Options)
        allowMethod(HttpMethod.Put)
        allowMethod(HttpMethod.Delete)
        allowMethod(HttpMethod.Patch)
        allowHeader(HttpHeaders.Authorization)
        allowHost("client-host")
        allowHost("client-host:8081")
        allowHost("client-host", subDomains = listOf("en", "de", "es"))
        allowHost("client-host", schemes = listOf("http", "https"))
    }
}

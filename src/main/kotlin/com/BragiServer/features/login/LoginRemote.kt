package com.BragiServer.features.login

import kotlinx.serialization.Serializable


@Serializable
data class LoginReceiveRemote(
    var email: String,
    var password:String,
)

@Serializable
data class LoginResponseRemote(
    val token: String,
)
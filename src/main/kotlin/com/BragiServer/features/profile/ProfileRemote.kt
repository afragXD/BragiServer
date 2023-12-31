package com.BragiServer.features.profile

import kotlinx.serialization.Serializable


@Serializable
data class ProfileResponseRemote(
    val email: String,
    val username: String,
    val gender: Boolean,
    val avatar: String,
)
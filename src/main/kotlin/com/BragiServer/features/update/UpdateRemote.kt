package com.BragiServer.features.update

import kotlinx.serialization.Serializable

@Serializable
data class UpdateReceiveRemote(
    var updateValue: String,
)

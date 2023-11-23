package com.BragiServer.features.books

import kotlinx.serialization.Serializable


@Serializable
data class BooksMenuReceiveRemote(
    var limit: Int,
)

@Serializable
data class BooksMenuResponseRemote(
    val id: Int,
    val name: String,
    val image: String,
    val rating: Float,
    val status: String,
)

@Serializable
data class BooksDetailResponseRemote(
    val name: String,
    val enName: String,
    val image: String,
    val description: String,
    val rating: Float,
    val status: String,
    val chapters: Short,
    val year: Short,
    val author: String,
)
package com.BragiServer.database.books

import kotlinx.serialization.Serializable


@Serializable
class BooksDTO(
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
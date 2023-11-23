package com.BragiServer.features.books

import com.BragiServer.features.login.LoginController
import io.ktor.server.application.*
import io.ktor.server.routing.*

fun Application.configureBooksRouting() {
    routing {
        get("/books/menu") {
            val booksController = BooksMenuController(call)
            booksController.menuBooks()
        }
        get("/books/detail") {
            val booksController = BooksDetailController(call)
            booksController.book()
        }
        get("/books/search") {
            val booksSearchController = BooksSearchController(call)
            booksSearchController.bookSearch()
        }
    }
}
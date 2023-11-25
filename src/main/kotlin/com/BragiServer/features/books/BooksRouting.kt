package com.BragiServer.features.books

import io.ktor.server.application.*
import io.ktor.server.routing.*

fun Application.configureBooksRouting() {
    // контроллер 1 действия
    routing {
        route("/books"){
            get("/menu") {
                val booksController = BooksMenuController(call)
                booksController.menuBooks()
            }
            get("/{id}/detail") {
                val booksController = BooksDetailController(call)
                booksController.book()
            }
            get("/search") {
                val booksSearchController = BooksSearchController(call)
                booksSearchController.bookSearch()
            }
        }
    }
}
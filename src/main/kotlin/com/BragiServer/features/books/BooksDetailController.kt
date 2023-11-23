package com.BragiServer.features.books

import com.BragiServer.database.books.Books
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.response.*

class BooksDetailController(val call: ApplicationCall) {
    suspend fun book(){

        val receive = call.request.queryParameters["id"]
        if (receive != null){
            val booksList = Books.getForId(receive.toInt())
            if (booksList != null){
                call.respond(booksList)
            }else{
                call.respond(HttpStatusCode.NotFound, "Нет книги с таким id")
            }
        }else{
            call.respond(HttpStatusCode.BadRequest, "Некорректный запрос")
        }

    }
}
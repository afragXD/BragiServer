package com.BragiServer.features.books

import com.BragiServer.database.books.Books
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.response.*
import org.jetbrains.exposed.sql.SortOrder

class BooksSearchController(val call: ApplicationCall) {
    suspend fun bookSearch(){

        val queryName = call.request.queryParameters["name"]
        val queryLimit = call.request.queryParameters["limit"]
        val sortReq = call.request.queryParameters["sort"]

        var sort: SortOrder = SortOrder.DESC
        if (sortReq.equals("ASC"))
            sort = SortOrder.ASC

        if (queryName != null && queryLimit != null){
            val booksList = Books.searchFromName(queryName, queryLimit.toInt(), sort)
            if (booksList.isNotEmpty()){
                call.respond(booksList)
            }else{
                call.respond(HttpStatusCode.NotFound, "Нет книги с таким названием")
            }
        }else if (queryName != null){
            val booksList = Books.searchFromName(queryName, 10, sort)
            if (booksList.isNotEmpty()){
                call.respond(booksList)
            }else{
                call.respond(HttpStatusCode.NotFound, "Нет книги с таким названием")
            }
        } else{
            call.respond(HttpStatusCode.BadRequest, "Некорректный запрос")
        }

    }
}
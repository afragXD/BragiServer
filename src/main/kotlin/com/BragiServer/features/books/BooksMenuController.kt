package com.BragiServer.features.books

import com.BragiServer.database.books.Books
import io.ktor.server.application.*
import io.ktor.server.response.*
import org.jetbrains.exposed.sql.SortOrder

class BooksMenuController(val call: ApplicationCall) {
    suspend fun menuBooks(){

        val limit = call.request.queryParameters["limit"]
        val sortReq = call.request.queryParameters["sort"]
        var sort: SortOrder = SortOrder.DESC
        if (sortReq.equals("ASC"))
            sort = SortOrder.ASC

        if (limit != null){
            val booksList = Books.getMenuBooks(limit.toInt(), sort)
            call.respond(booksList)
        }else{
            val booksList = Books.getMenuBooks(10, sort)
            call.respond(booksList)
        }


    }
}
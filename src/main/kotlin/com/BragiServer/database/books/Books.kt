package com.BragiServer.database.books

import com.BragiServer.features.books.BooksDetailResponseRemote
import com.BragiServer.features.books.BooksMenuResponseRemote
import com.BragiServer.utils.StringMatch
import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.SqlExpressionBuilder.eq
import org.jetbrains.exposed.sql.transactions.transaction
import java.util.*

object Books: Table() {
    private val id = Books.integer("id")
    private val name = Books.text("name")
    private val enName = Books.text("en_name")
    private val image = Books.text("image")
    private val description = Books.text("description")
    private val rating = Books.float("rating")
    private val status = Books.varchar("status", 15)
    private val chapters = Books.short("chapters")
    private val year = Books.short("year")
    private val author = Books.text("author")

    fun getMenuBooks(limit: Int, sort: SortOrder): List<BooksMenuResponseRemote>{
        return try {
            transaction {
                Books.selectAll()
                    .limit(limit)
                    .orderBy(rating to sort)
                    .toList()
                    .map {
                        BooksMenuResponseRemote(
                            id = it[Books.id],
                            name = it[name],
                            image = it[image],
                            rating = it[rating],
                            status = it[status],
                        )
                    }
            }
        }catch (e: Exception){
            emptyList()
        }
    }

    fun getForId(id:Int): BooksDetailResponseRemote? {
        return try {
            transaction {
                val bookModel = Books.select { Books.id.eq(id) }.single()
                BooksDetailResponseRemote(
                    name = bookModel[name],
                    enName = bookModel[enName],
                    image = bookModel[image],
                    description = bookModel[description],
                    rating = bookModel[rating],
                    status = bookModel[status],
                    chapters = bookModel[chapters],
                    year = bookModel[year],
                    author = bookModel[author],
                )
            }
        }catch (e: Exception){
            null
        }
    }

    fun searchFromName(name: String, limit: Int, sort: SortOrder): List<BooksMenuResponseRemote> {
        return try {
            transaction {
                Books.select{
                    Books.name.lowerCase() like "%${name.lowercase(Locale.getDefault())}%"
                }
                    .limit(limit).orderBy(rating to sort)
                    .toList()
                    .map {
                        BooksMenuResponseRemote(
                            id = it[Books.id],
                            name = it[Books.name],
                            image = it[image],
                            rating = it[rating],
                            status = it[status],
                        )
                    }
            }
        }catch (e: Exception){
            emptyList()
        }
    }
}
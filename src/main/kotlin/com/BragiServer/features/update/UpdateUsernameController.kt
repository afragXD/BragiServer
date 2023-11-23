package com.BragiServer.features.update

import com.BragiServer.database.tokens.Tokens
import com.BragiServer.database.user.Users
import com.BragiServer.utils.TokenCheck
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*

class UpdateUsernameController(val call: ApplicationCall) {

    suspend fun updateUsername(){
        val token = call.request.headers["Bearer-Authorization"]
        val receive = call.receive<UpdateReceiveRemote>()

        if (TokenCheck.isTokenValid(token.orEmpty())){
            val tokenDTO = Tokens.fetchTokens1(token.toString())
            val userDTO = tokenDTO?.let { Users.fetchUser(it.email) }
            if (userDTO != null) {
                Users.fetchUpdateUsername(userDTO.email, receive.updateValue)
                call.respondText("Данные обновлены")
                //call.respond(HttpStatusCode.BadGateway, "Ошибка авторизации")
            }
        }else{
            if (token == null){
                call.respond(HttpStatusCode.Forbidden, "Ошибка входа")
            }else {
                Tokens.fetchOut(token)
                call.respond(HttpStatusCode.Unauthorized, "Срок действия токена истек")
            }
        }

    }

}
package com.BragiServer.features.profile

import com.BragiServer.database.tokens.Tokens
import com.BragiServer.database.user.Users
import com.BragiServer.utils.TokenCheck
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*

class ProfileController(private val call: ApplicationCall) {
    suspend fun profileSearch(){
        val token = call.request.headers["Bearer-Authorization"]
        if (TokenCheck.isTokenValid(token.orEmpty())){
            val tokenDTO = Tokens.fetchTokens1(token.toString())
            val userDTO = tokenDTO?.let { Users.fetchUser(it.email) }
            if (userDTO != null) {
                call.respond(
                    ProfileResponseRemote(
                        email = userDTO.email,
                        username = userDTO.username,
                        gender = userDTO.gender,
                        avatar = userDTO.avatar,
                    )
                )
            }
        }else{
            if (token == null){
                call.respond(HttpStatusCode.Forbidden, "Еблан входа")
            }else {
                Tokens.fetchOut(token)
                call.respond(HttpStatusCode.Unauthorized, "Срок действия токена истек")
            }
        }
    }
}
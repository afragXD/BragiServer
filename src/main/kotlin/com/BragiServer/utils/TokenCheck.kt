package com.BragiServer.utils

import com.BragiServer.database.tokens.Tokens
import com.auth0.jwt.JWT
import com.auth0.jwt.JWTVerifier
import com.auth0.jwt.algorithms.Algorithm
import com.auth0.jwt.exceptions.TokenExpiredException

object TokenCheck {
    fun isTokenValid(token:String?):Boolean {

        val jwtSecret = System.getenv("JWT_SECRET")
        val algorithm = Algorithm.HMAC512(jwtSecret)

        val verifier: JWTVerifier = JWT.require(algorithm).build()

        return try {
            val jwt = verifier.verify(token)
            val exceptionTime = jwt.expiresAt
            val currentTime = System.currentTimeMillis()

            if (exceptionTime != null && exceptionTime.time < currentTime){
                false
            }else{
                (Tokens.fetchTokens().firstOrNull{it.token == token} != null)
            }
        }catch (error: TokenExpiredException){
            false
        }catch (error: Exception){
            false
        }

    }
}
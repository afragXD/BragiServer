package com.BragiServer.utils

import com.BragiServer.database.tokens.Tokens
import com.auth0.jwt.JWT
import com.auth0.jwt.JWTVerifier
import com.auth0.jwt.algorithms.Algorithm
import com.auth0.jwt.exceptions.TokenExpiredException

object StringMatch {
    fun isStrMatch(str1:String, str2:String):Float {
        val matrix = Array(str1.length + 1) {
            Array(str2.length + 1) { 0 }
        }

        for (i in 0..str1.length) {
            matrix[i][0] = i
        }

        for (i in 0..str2.length) {
            matrix[0][i] = i
        }

        for (i in 1..str1.length) {
            for (j in 1..str2.length) {
                if (str1[i - 1] == str2[j - 1]) {
                    matrix[i][j] = matrix[i - 1][j - 1]
                } else {
                    matrix[i][j] = Integer.min(Integer.min(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1]) + 1
                }
            }
        }

        val levenshteinDistance = matrix[str1.length][str2.length]
        val maxLength = maxOf(str1.length, str2.length)
        val matchPercentage = (1 - (levenshteinDistance.toFloat() / maxLength)) * 100

        return matchPercentage
    }
}
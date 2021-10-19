package com.example.hackathonapp

import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

interface RetrofitInterface {
    @POST("/health")
    fun getResult(@Body map: HashMap<String?,String?>?) : Call<Result?>?
}
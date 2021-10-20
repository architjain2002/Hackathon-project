package com.example.hackathonapp

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.AutoCompleteTextView
import android.widget.Toast
import androidx.core.view.isVisible
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.result.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import okhttp3.OkHttpClient
import java.util.concurrent.TimeUnit


class MainActivity : AppCompatActivity() {
    private var retrofitInterface: RetrofitInterface? = null
    private val BASE_URL = "http://10.0.2.2:3000"
    var client = OkHttpClient.Builder()
        .connectTimeout(100, TimeUnit.SECONDS)
        .readTimeout(100, TimeUnit.SECONDS).build()
    private  val retrofit: Retrofit? = Retrofit.Builder()
        .baseUrl(BASE_URL).client(client)
        .addConverterFactory(GsonConverterFactory.create())
        .build()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        retrofitInterface = retrofit!!.create(RetrofitInterface::class.java)
        val symptoms1 = resources.getStringArray(R.array.symptom1)
        val symptoms2 = resources.getStringArray(R.array.symptom2)
        val symptoms3 = resources.getStringArray(R.array.symptom3)

        val arrayAdapter1 = ArrayAdapter(this, R.layout.dropdown_item, symptoms1)
        val arrayAdapter2 = ArrayAdapter(this, R.layout.dropdown_item, symptoms2)
        val arrayAdapter3 = ArrayAdapter(this, R.layout.dropdown_item, symptoms3)

        val autocompleteTV = findViewById<AutoCompleteTextView>(R.id.autoCompleteTextView)
        val autocompleteTV2 = findViewById<AutoCompleteTextView>(R.id.autoCompleteTextView2)
        val autocompleteTV3 = findViewById<AutoCompleteTextView>(R.id.autoCompleteTextView3)

        autocompleteTV.setAdapter(arrayAdapter1)
        autocompleteTV2.setAdapter(arrayAdapter2)
        autocompleteTV3.setAdapter(arrayAdapter3)

        button.setOnClickListener {
            progressBar.isVisible = true
            textView6.isVisible = true
            textInputLayout.isVisible = false
            textInputLayout2.isVisible = false
            textInputLayout3.isVisible =false
            button.isVisible = false
             getResult()
        }

    }

    private fun getResult(){
        val map = HashMap<String?,String?>()
        map["Symptom_1"] = autoCompleteTextView.text.toString()
        map["Symptom_2"] = autoCompleteTextView2.text.toString()
        map["Symptom_3"] = autoCompleteTextView3.text.toString()
        val call = retrofitInterface!!.getResult(map)
        call!!.enqueue( object : Callback<Result?> {
            override fun onResponse(call: Call<Result?>, response: Response<Result?>) {
                progressBar.isVisible = false
                textView6.isVisible = false
                setContentView(R.layout.result)
                button2.setOnClickListener {
                    startActivity(Intent(this@MainActivity,MainActivity::class.java))
                }
                if(response.code() == 200) {
                    val rep = response.body()
                    textView2.text = "Precautions that you can take :-\n"+rep!!.precautions_1 + "\n" + rep.precautions_2 + "\n" + rep.precautions_3 + "\n" + rep.precautions_4
                    textView3.text = "Disease:-\n"+rep.disease
                    textView4.text = "Description of the disease:-\n"+rep.description
                    Toast.makeText(this@MainActivity,"Successfully added",Toast.LENGTH_SHORT).show()
                }else{
                    Toast.makeText(this@MainActivity,"Some error occured", Toast.LENGTH_SHORT).show()
                }
            }
            override fun onFailure(call: Call<Result?>, t: Throwable) {
                Toast.makeText(applicationContext, t.toString(), Toast.LENGTH_LONG).show();
            }
        });
    }
}
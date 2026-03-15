//
//for form Data
for (let pair of formData.entries()) {
          console.log(pair[0], pair[1]);
        }

//api file 

print("POST:", request.POST)
print("FILES:", request.FILES)

//api request
const token = await getAccessToken()
console.log("TOKEN BEING SENT:", token)


//listing dependencies
cat package.json
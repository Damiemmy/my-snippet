1.
//
//for form Data
for (let pair of formData.entries()) {
          console.log(pair[0], pair[1]);
        }

2.
//api file 

print("POST:", request.POST)
print("FILES:", request.FILES)

3.
//api request
const token = await getAccessToken()
console.log("TOKEN BEING SENT:", token)

4.

//listing dependencies
cat package.json


5. //fixing dependencies and vulnerability on nextjs

/* fix available via `npm audit fix --force`
 Will install next@15.5.12, which is outside the stated dependency range*/
 //solution
npm audit
npm audit fix 
npm install next@latest
npm audit // to check if the error has finnaly been fixed

const mongodb = require("mongodb").MongoClient;
const csvtojson = require("csvtojson");

let url = "mongodb://localhost:27017/";

csvtojson()
  .fromFile("userDetails.csv")  //name of csv
  .then(csvData => {
    console.log(csvData);

    mongodb.connect(
      url,
      { useNewUrlParser: true, useUnifiedTopology: true },
      (err, client) => {
        if (err) throw err;

        client
          .db("newDB")  //name of the db
          .collection("userDetails")	//name of the collection: for existng collection, the contents are appended at the end.
          .insertMany(csvData, (err, res) => {
            if (err) throw err;

            console.log(`Inserted: ${res.insertedCount} rows`);
            client.close();
          });
       
          
      }
    );
  });

/*****Code to delete the collection: Uncomment only if required
mongodb.connect(
  url,
  { useNewUrlParser: true, useUnifiedTopology: true },
  (err, client) => {
		 client
          .db("newDB")
          .collection("userDetails")
		  .drop( (err , collection) => {
		if(err) throw err;
		if(collection) console.log("Dropped successfully");
		client.close();
	});
    }
    );
**********************/

	

import React from 'react'
import { LineChart } from 'react-chartkick'
import 'chart.js'
import * as tempData from './data/tempData.json'

function MyChart() {
  let temperatureData = '{}'
  let humidityData = "{}"
  let dataArray = tempData
  console.log(dataArray)
  for (let i =0; i < dataArray.length; i++){
    temperatureData = temperatureData.split("}")[0] + '"' + dataArray[i].datetime + '": ' + dataArray[i].temp + ",}"
    humidityData = humidityData.split("}")[0] + dataArray[i].datetime + ":" + dataArray[i].humid + ",}"
  }
  console.log(JSON.stringify(temperatureData))
  
let data = [
  {
    "name":"Temperatur (C°)", "data": {"2017-05-13": 60, "2017-06-14": 5, "2018-07-14": 5, "2019-05-14": 15, "2019-05-30": 5, "2020-05-14": 25}
  },
  {
    "name":"Luftfuktigehet (%)","data": {"2017-05-13": 60, "2017-06-14": 5, "2018-07-14": 5, "2019-05-14": 15, "2019-05-30": 5, "2020-05-14": 25}
  }
]

console.log(data)
console.log(tempData.default)
return ( 
  <div>
    <LineChart min={0} max={100} width="1024px" height="800px" data={tempData.default} />
  </div>
);
}

export default MyChart
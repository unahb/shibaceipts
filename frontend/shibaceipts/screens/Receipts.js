import React, { useEffect, useState } from 'react'
import { FlatList, Text, View, StyleSheet } from 'react-native'
import { Card, Button, Image } from 'react-native-elements'
import { useIsFocused } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import {MockReceipts} from '../mock_backend'
import { NavigationContainer } from '@react-navigation/native'
import { MOCKDATA, APILOCATION } from '../constants'
// import { APILOCATION } fr/om '../constants'

// import { SingularReceipt } from './SingularReceipt'

const Stack = createNativeStackNavigator();

const styles = StyleSheet.create({
  singularReceipt: {
    width: 1000,
    height: 1000,
    resizeMode: 'stretch'
  }
})



const renderReceiptCard = (item, navigation) => {
  return (
    <Card>
      {/* Marc help, why is this item.item nested??! */}
      <Card.Image source={{uri: `${APILOCATION}${item.imgpath}`}} onPress={()=>navigation.navigate("SingularReceipt", item)}/>
    </Card>
  )
}

function ReceiptsList({navigation}) {
  const [receipts, setReceipts] = useState([])
  
  const isFocused = useIsFocused()

  useEffect(() => {
    if (MOCKDATA) setReceipts(MockReceipts)
    else {
      fetch(`${APILOCATION}get-current-user-receipts`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((json) => setReceipts(json.data))
    }
  }, [isFocused])

  useEffect(() => {
    if (MOCKDATA) setReceipts(MockReceipts)
    else {
      fetch(`${APILOCATION}get-current-user-receipts`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((json) => setReceipts(json.data))
    }
  }, [])

  return (
      <FlatList
          data={receipts}
          keyExtractor={(item) => item.location}
          renderItem={item => renderReceiptCard(item.item, navigation)}
      />
  )
}

function SingularReceipt({route}) {
  const { receipt, imgpath } = route.params
  const entries = Object.entries(receipt)
  const uri = `${APILOCATION}${imgpath}`
  return (
    <View>
      <Image style={styles.singularReceipt} source={{uri}}></Image>
      <FlatList
        data={entries}
        // Not guaranteed to be unique?
        keyExtractor={(item) => item[0]}
        renderItem={r => {
          const item_name = r.item[0]
          const item_price = r.item[1]
          return (<Text>{item_name} - {item_price}</Text>)
        }}
      />
    </View>
  )
}

export default function Receipts() {
  return (
      <Stack.Navigator>
          <Stack.Screen name="Receipts List" component={ReceiptsList}></Stack.Screen>
          <Stack.Screen name="SingularReceipt" component={SingularReceipt}></Stack.Screen>
      </Stack.Navigator>
  )
}
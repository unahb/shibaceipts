import React from 'react'
import { FlatList, Text } from 'react-native'
import { Card, Button } from 'react-native-elements'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import {MockReceipts} from '../mock_backend'
import { NavigationContainer } from '@react-navigation/native'

// import { SingularReceipt } from './SingularReceipt'

const Stack = createNativeStackNavigator();

const renderReceiptCard = (item, navigation) => {
  return (
    <Card>
      {/* Marc help, why is this item.item nested??! */}
      <Card.Title>{item.item.receipt.date}</Card.Title> <Card.Divider />{' '}
      <Card.Image source={{uri: item.item.receipt.image}}></Card.Image>
      <Button title="More Info"
        onPress={()=>navigation.navigate("SingularReceipt",
        {text: item.item.receipt.text})}/>
    </Card>
  )
}

function ReceiptsList({navigation}) {
    return (
        <FlatList
            data={MockReceipts}
            keyExtractor={(item) => item.key}
            renderItem={(item) => renderReceiptCard(item, navigation)}
        />
    )
}

function SingularReceipt({route}) {
  const { text } = route.params;
  return (
      <Text>{text}</Text>
  )
}

export default function Receipts() {
  return (
      <Stack.Navigator>
          <Stack.Screen name="Receipts" component={ReceiptsList}></Stack.Screen>
          <Stack.Screen name="SingularReceipt" component={SingularReceipt}></Stack.Screen>
      </Stack.Navigator>
  )
}
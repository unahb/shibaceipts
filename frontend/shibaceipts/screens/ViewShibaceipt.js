import React from 'react'
import { View, StyleSheet } from 'react-native'
import { Image, Text, Card, Button, Icon } from 'react-native-elements'
import Countdown from 'react-countdown'

import { APILOCATION } from '../constants'

export default function ViewShibaceipt({ route }) {
  return (
    <View style={{ alignItems: 'center' }}>
      <Image source={{ uri: route.params.location }} style={{ width: 300, height: 300 }} />
      {route.params.expiration ?
      <Card>
        {' '}
        <Card.Title style={{ fontSize: '30px' }}>Price: {route.params.value}Ð</Card.Title> <Card.Divider />
        <Text style={{ fontSize: 15 }}>
          ⏳ Time Remaining: <Countdown date={route.params.expiration} />
        </Text>
        <Button
          icon={<Icon style={{ marginRight: 5 }} name='payments' color='#ffffff' />}
          buttonStyle={{ borderRadius: 0, marginLeft: 0, marginRight: 0, marginBottom: 0, marginTop: 5 }}
          title='BUY NOW'
          onPress={() => {
            var formData = new FormData()
            formData.append('price', route.params.value)
            formData.append('shibaceipt', route.params.location)

            fetch(`${APILOCATION}purchase-shibaceipt`, {
              method: 'POST',
              body: formData,
            })
          }}
        />
      </Card>
      :
        <Button icon={<Icon style={{ marginRight: 5 }} name='payments' color='#ffffff' />} buttonStyle={{ borderRadius: 0, marginLeft: 0, marginRight: 0, marginBottom: 0, marginTop: 5 }} title='SELL NOW' />
      }
      <Text style={styles.Text}>Owner: {route.params.owner}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  Text: {
    marginTop: 10,
    fontSize: 20,
  },
})
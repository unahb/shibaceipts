import React from 'react'
import { View, StyleSheet } from 'react-native'
import { Image, Text, Card, Button, Icon } from 'react-native-elements'
import Countdown from 'react-countdown'

export default function ViewShibaceipt({ route }) {
  return (
    <View style={{ alignItems: 'center' }}>
      <Image source={{ uri: route.params.location }} style={{ width: 300, height: 300 }} />
      <Card>
        {' '}
        <Card.Title style={{ fontSize: '30px' }}>Price: {route.params.value}Ð</Card.Title> <Card.Divider />
        <Text style={{ fontSize: 15 }}>
          ⏳ Time Remaining: <Countdown date={route.params.expiration} />
        </Text>
        <Button icon={<Icon style={{ marginRight: 5 }} name='payments' color='#ffffff' />} buttonStyle={{ borderRadius: 0, marginLeft: 0, marginRight: 0, marginBottom: 0, marginTop: 5 }} title='BUY NOW' />
      </Card>
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
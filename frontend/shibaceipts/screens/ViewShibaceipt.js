import React from 'react'
import { View, StyleSheet } from 'react-native'
import { Image, Text } from 'react-native-elements'

export default function ViewShibaceipt({ route }) {
  return (
    <View style={{ alignItems: 'center' }}>
      <Image source={{ uri: route.params.location }} style={{ width: 300, height: 300 }} />
      <Text style={styles.Text}>Owner: {route.params.owner}</Text>
      <Text style={styles.Text}>Minter: {route.params.minter}</Text>
      <Text style={styles.Text}>Value: {route.params.value}</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  Text: {
    fontSize: '20px',
  },
})
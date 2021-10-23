import React from 'react'
import { FlatList, View } from 'react-native'
import { Card, Button, Icon, Text, Image } from 'react-native-elements'
import { MockPosts } from '../mock_backend'

const renderItem = (item) => {
  return (
    <Card>
      <View style={{ alignItems: 'center' }}>
        <Card.Title>
          <View style={{ flexDirection: 'row', alignItems: 'center' }}>
            <Image resizeMode='cover' source={{ uri: item.user.avatar }} style={{ width: 50, height: 50, borderRadius: '50%', marginRight: '15px' }} />
            <Text>{item.user.username}</Text>{' '}
          </View>
        </Card.Title>
        <Card.Image source={{ uri: item.shibaceipt }} style={{ width: 200, height: 200 }}></Card.Image>
      </View>
    </Card>
  )
}

export default function Home() {
  return <FlatList data={MockPosts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item)} />
}

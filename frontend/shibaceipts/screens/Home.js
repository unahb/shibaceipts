import React from 'react'
import { FlatList } from 'react-native'
import { Card, Button, Icon } from 'react-native-elements'
import {MockPosts} from '../mock_backend'

const renderItem = (item) => {
  return (
    <Card>
      <Card.Title>{item.user.username}</Card.Title> <Card.Divider />{' '}
      <Card.Image source={{uri: item.shibaceipt}}>
      </Card.Image>
    </Card>
  )
}

export default function Home() {
  return (
      <FlatList
        data={MockPosts}
        keyExtractor={(item) => item.shibaceipt}
        renderItem={({ item }) => renderItem(item)}
      />
  )
}

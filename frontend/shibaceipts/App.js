import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'

const Drawer = createDrawerNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen
          name='Home'
          component={Home}
          options={{
            drawerLabel: 'Home',
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}


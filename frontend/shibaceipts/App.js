import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createDrawerNavigator } from '@react-navigation/drawer'

import Home from './screens/Home'
import Receipts from './screens/Receipts'

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
        <Drawer.Screen
          name='Receipts'
          component={Receipts}
          options={{
            drawerLabel: 'Receipts',
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  )
}


import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css'; // Import the styles
import MyFavsTab from '../MyFavsTab';
import HorrorTab from '../HorrorTab';
import ActionTab from './ActionTab';
import RomanceTab from '../RomanceTab';
import SciFiTab from '../SciFiTab';
import ComedyTab from '../ComedyTab';
import './App.css'; // Create this file for your own styles

const App = () => {
  const [tabIndex, setTabIndex] = useState(0);

  const handleTabSelect = (index) => {
    setTabIndex(index);
  };

  return (
    <div>
      <Tabs selectedIndex={tabIndex} onSelect={handleTabSelect}>
        <TabList>
          <Tab>my Favs</Tab>
          <Tab>Horror</Tab>
          <Tab>Action</Tab>
          <Tab>Romance</Tab>
          <Tab>Sci-Fi</Tab>
          <Tab>Comedy</Tab>
        </TabList>

        <TabPanel>
          {/* Content for Tab 1 */}
          <MyFavsTab />
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 2 */}
          <HorrorTab />
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 3 */}
          <ActionTab />
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 4 */}
          <RomanceTab />
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 5 */}
          <SciFiTab />
        </TabPanel>
        <TabPanel>
          {/* Content for Tab 6 */}
          <ComedyTab />
        </TabPanel>
      </Tabs>
    </div>
  );
};

export default App;

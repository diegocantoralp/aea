# aea
<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-jar-plugin</artifactId>
				<version>3.4.2</version>
				<configuration>
					<archive>
						<manifest>
							<addDefaultImplementationEntries>true</addDefaultImplementationEntries>
							<mainClass>SenderEF</mainClass>
						</manifest>
					</archive>
				</configuration>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-shade-plugin</artifactId>
				<version>3.2.4</version>
				<executions>
					<execution>
						<phase>package</phase>
						<goals>
							<goal>shade</goal>
						</goals>
					</execution>
				</executions>
			</plugin>

